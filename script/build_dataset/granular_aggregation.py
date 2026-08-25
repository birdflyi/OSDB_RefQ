#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3.9

# @Time   : 2026/1/17 17:41
# @Author : 'Lou Zehua'
# @File   : granular_aggregation.py

import json

import numpy as np
import pandas as pd
from GH_CoRE.model import Attribute_getter, ObjEntity
from GH_CoRE.working_flow.body_content_preprocessing import read_csvs

from etc import filePathConf
from script.build_dataset.repository_identity_provenance import (
    ADMITTED_SOURCE_OBSERVATION,
    INVALID_EVENT_REPOSITORY_ID,
    admit_source_record,
    normalize_repository_id,
)


def granu_agg(row: pd.Series, repo_id=None):
    if row["src_entity_type"] == "Actor":
        row["src_entity_id_agg"] = row["src_entity_id"]
        row["src_entity_type_agg"] = row["src_entity_type"]
    else:
        row["src_entity_id_agg"] = "R_" + str(repo_id)
        row["src_entity_type_agg"] = "Repo"

    tar_entity_id_agg = None
    tar_entity_type_agg = "Object"
    tar_entity_objnt_prop_dict = parse_tar_entity_objnt_prop_dict(row["tar_entity_objnt_prop_dict"])
    if tar_entity_objnt_prop_dict:
        if "repo_id" in tar_entity_objnt_prop_dict.keys():
            if tar_entity_objnt_prop_dict["repo_id"] is not None:  # Except for unknown sha like fragment
                tar_entity_id_agg = "R_" + str(tar_entity_objnt_prop_dict["repo_id"])
                tar_entity_type_agg = "Repo"
        elif "actor_id" in tar_entity_objnt_prop_dict.keys():
            if tar_entity_objnt_prop_dict["actor_id"] is not None:
                tar_entity_id_agg = "A_" + str(tar_entity_objnt_prop_dict["actor_id"])
                tar_entity_type_agg = "Actor"
        else:
            pass  # can not parse
    row["tar_entity_id_agg"] = tar_entity_id_agg
    row["tar_entity_type_agg"] = tar_entity_type_agg
    return row


def granu_agg_with_event_provenance(
    row: pd.Series,
    expected_source_context_repo_id=None,
    *,
    require_event_repo_id: bool = True,
):
    """Aggregate a row using authoritative event repository provenance.

    This is the opt-in v2 path. The historical ``granu_agg`` function remains
    unchanged for v1 materializations. For a non-Actor source, the aggregate
    repository is derived from ``row.event_repo_id``. The expected seed ID is
    retained only as context and admission assertion.
    """

    result = row.copy()
    if "event_repo_id" not in result.index:
        if require_event_repo_id:
            raise KeyError("event_repo_id is required for provenance-aware aggregation")
        event_repo_id = None
    else:
        try:
            event_repo_id = normalize_repository_id(
                result.get("event_repo_id"),
                field_name="event_repo_id",
            )
        except ValueError:
            event_repo_id = None
            admission_status = INVALID_EVENT_REPOSITORY_ID
        else:
            admission = admit_source_record(event_repo_id, expected_source_context_repo_id)
            admission_status = admission.status

    if "admission_status" not in locals():
        admission = admit_source_record(event_repo_id, expected_source_context_repo_id)
        admission_status = admission.status

    result["event_repo_id"] = event_repo_id
    result["expected_source_context_repo_id"] = normalize_repository_id(
        expected_source_context_repo_id,
        field_name="expected_source_context_repo_id",
    )
    result["source_admission_status"] = admission_status
    result["source_provenance_mismatch"] = admission_status != ADMITTED_SOURCE_OBSERVATION

    if result.get("src_entity_type") == "Actor":
        result["src_entity_id_agg"] = result.get("src_entity_id")
        result["src_entity_type_agg"] = result.get("src_entity_type")
    elif event_repo_id is not None:
        result["src_entity_id_agg"] = "R_" + event_repo_id
        result["src_entity_type_agg"] = "Repo"
    else:
        result["src_entity_id_agg"] = None
        result["src_entity_type_agg"] = "Repo"

    source_aggregate = result["src_entity_id_agg"]
    source_aggregate_type = result["src_entity_type_agg"]

    # Reuse the historical target parser without allowing its caller argument
    # to overwrite the already-set event-derived source aggregate.
    target_aggregate = granu_agg(result, repo_id=event_repo_id)
    target_aggregate["src_entity_id_agg"] = source_aggregate
    target_aggregate["src_entity_type_agg"] = source_aggregate_type
    target_aggregate["event_repo_id"] = result["event_repo_id"]
    target_aggregate["expected_source_context_repo_id"] = result["expected_source_context_repo_id"]
    target_aggregate["source_admission_status"] = result["source_admission_status"]
    target_aggregate["source_provenance_mismatch"] = result["source_provenance_mismatch"]
    return target_aggregate


def set_entity_type_fine_grained(row: pd.Series):
    ent_type = "GitHub_Service_External_Links"
    tar_entity_objnt_prop_dict = parse_tar_entity_objnt_prop_dict(row["tar_entity_objnt_prop_dict"])
    need_check_objnt_prop = isinstance(tar_entity_objnt_prop_dict, dict) and ("repo_id" in tar_entity_objnt_prop_dict.keys() or "actor_id" in tar_entity_objnt_prop_dict.keys())
    if not need_check_objnt_prop:  # GitHub_Other_Service and GitHub_Service_External_Links and other wrong pattern has no id
        if row["tar_entity_match_pattern_type"] in ["GitHub_Other_Service", "GitHub_Service_External_Links"]:
            ent_type = row["tar_entity_match_pattern_type"]
        else:
            pass  # Can not get a valid node response from GitHub REST API or GitHub GraphQL. Regard as GitHub_Service_External_Links.
    else:  # row["tar_entity_type"] have Fine grained type when row["tar_entity_type"] != "Object", especially for Issue_PR and SHA pattern
        if row["tar_entity_type"] == "Object":
            ent_type = row["tar_entity_match_pattern_type"]
            if ent_type == "Issue_PR":
                if isinstance(tar_entity_objnt_prop_dict, dict):
                    repo_id = tar_entity_objnt_prop_dict.get("repo_id")
                    issue_number = tar_entity_objnt_prop_dict.get("issue_number")
                    if repo_id and issue_number:
                        row["tar_entity_type"] = Attribute_getter.__get_issue_type(repo_id, issue_number)
                        ent_type = row["tar_entity_type"]
                        tar_entity = ObjEntity(ent_type)
                        tar_entity.set_val(tar_entity_objnt_prop_dict)
                        row["tar_entity_id"] = tar_entity.__repr__(brief=True) if tar_entity.__PK__ else None
        else:
            ent_type = row["tar_entity_type"]  # for Issue, IssueComment, PullRequest, PullRequestReviewComment and Commit
    row["tar_entity_type_fine_grained"] = ent_type
    return row


def parse_tar_entity_objnt_prop_dict(tar_entity_objnt_prop_dict_raw):
    tar_entity_objnt_prop_dict = None
    try:
        if np.isnan(float(tar_entity_objnt_prop_dict_raw)):
            tar_entity_objnt_prop_dict = None
    except:
        pass

    if pd.isna(tar_entity_objnt_prop_dict_raw):  # all of GitHub_Other_Service, GitHub_Service_External_Links
        pass
    else:
        try:
            tar_entity_objnt_prop_dict = dict(tar_entity_objnt_prop_dict_raw)
        except Exception:
            prop_str = str(tar_entity_objnt_prop_dict_raw)
            try:
                tar_entity_objnt_prop_dict = json.loads(prop_str)
            except json.JSONDecodeError:
                # Swap the two quotation marks and try to parse again
                prop_str = prop_str.replace('"', '$').replace("'", '"').replace('$', "'")
                try:
                    # if prop_str.startswith("'") and prop_str.endswith("'"):
                    #     prop_str = prop_str[1:-1].replace("'", '"')
                    tar_entity_objnt_prop_dict = json.loads(prop_str)
                except json.JSONDecodeError:
                    try:
                        tar_entity_objnt_prop_dict = dict(eval(prop_str))
                    except Exception:
                        prop_str = prop_str.replace("'", '"')  # Forced analysis with [\', \"] mixed mode
                        tar_entity_objnt_prop_dict = json.loads(prop_str)
    return tar_entity_objnt_prop_dict


if __name__ == '__main__':
    year = 2023
    # dbms_repos_key_feats_path = filePathConf.absPathDict[filePathConf.DBMS_REPOS_KEY_FEATS_PATH]
    # dbms_repos_raw_content_dir = filePathConf.absPathDict[filePathConf.DBMS_REPOS_RAW_CONTENT_DIR]
    # dbms_repos_dedup_content_dir = filePathConf.absPathDict[filePathConf.DBMS_REPOS_DEDUP_CONTENT_DIR]
    collaboration_relation_extraction_dir = filePathConf.absPathDict[filePathConf.DBMS_REPOS_GH_CORE_DIR]
    repo_names = ["pingcap/tidb", "tikv/tikv"]
    filenames = [f"{name.replace('/', '_')}_{str(year)}" for name in repo_names]
    df_dbms_repos_dict = read_csvs(collaboration_relation_extraction_dir, filenames=filenames, index_col=None)
    df_dbms_repo = df_dbms_repos_dict[filenames[0]]
    # relation filter
    df_dbms_repo = df_dbms_repo[df_dbms_repo["relation_type"] == "Reference"]
    # target node granular aggregation
    df_dbms_repo = df_dbms_repo.apply(granu_agg)
    # G_repo = build_collab_net(df_dbms_repo, src_tar_colnames=['src_entity_id', 'tar_entity_id'],
    #                           default_node_types=['src_entity_type', 'tar_entity_type'], default_edge_type="event_type",
    #                           init_record_as_edge_attrs=True, use_df_col_as_default_type=True, out_g_type='DG')
