#!/usr/bin/python
# -*- coding:utf-8 -*-

# TODO: Specify Docs of function, add Doc for File and variables
import json
from mariadb import Cursor


def get_all_keywords(cur:Cursor) -> list:
    cur.execute("SELECT primary_keywords, secondary_keywords FROM matching_table")
    keywords = []
    for primary_keywords, secondary_keywords in cur:
        kwords = primary_keywords.split(",")
        for kword in kwords:
            keywords.append(kword)
        kwords = secondary_keywords.split(",")
        for kword in kwords:
            keywords.append(kword)
    return keywords


# TODO: add checks for wrong returns, raise Error
def get_generic_term(synonym: str, cur:Cursor) -> str:
    """Searchs for the generic term of a synonym.

    ADD DESCRIPTION

    :param synonym: String of the word for which the generic term should be found.
    :return: Returns the generic term as string if there is one for the synonym.
    :raise RASENError: Generic term is not in the database table.
    """
    reqstr = f"SELECT id, synonym FROM synonyms WHERE synonym='{synonym}'"
    cur.execute(reqstr)
    synonym_id = None
    for (id, synonym) in cur:
        synonym_id = id
    if synonym_id is None:
        return None
    reqstr = f"SELECT generic_term, id FROM generic_terms WHERE id={synonym_id}"
    cur.execute(reqstr)
    gen_term = None
    for generic_term, id in cur:
        gen_term = generic_term
    return gen_term


# TODO: add check for wrong case_id, raise InvalidCaseIDError
def get_answer(case_id: int, cur:Cursor) -> str:
    """Returns the answer for case_id

    ADD DESCRIPTION

    :param case_id: Integer of the specific answer.
    :return: Returns the answer as string if there is one.
    :raise InvalidCaseIDError: case_id is not in the database table.
    """
    reqstr = f"SELECT answer FROM matching_table WHERE caseID={case_id}"
    cur.execute(reqstr)
    ans = None
    for answer in cur:
        ans = answer[0]
    return ans


def get_caseIDs_by_keywords(word: str, cur:Cursor):
    reqstr = f"SELECT caseID FROM matching_table WHERE primary_keywords LIKE '%{word}%' OR secondary_keywords LIKE '%{word}%'"
    cur.execute(reqstr)
    cID = []
    for (caseID) in cur:
        cID.append(caseID[0])
    if len(cID) == 0:
        return None
    return cID


def get_weight_of_keyword(keyword: str, cur:Cursor) -> float:
    reqstr = f"SELECT weight FROM weights WHERE keyword='{keyword}'"
    cur.execute(reqstr)
    wgt = None
    for weight in cur:
        wgt = weight[0]
    if wgt is None:
        wgt = 0
    return wgt


def get_primary_keywords_by_caseID(caseID: int, cur:Cursor):
    reqstr = f"SELECT primary_keywords FROM matching_table WHERE caseID='{caseID}'"
    cur.execute(reqstr)
    pri_key = None
    for (primary_keywords) in cur:
        pri_key = primary_keywords[0]
    return pri_key


def get_weights(cur:Cursor):
    reqstr = f"SELECT keyword, weight FROM weights"
    cur.execute(reqstr)
    weights = []
    for keyword, weight in cur:
        weights.append({'keyword': keyword, 'weight': weight})
    json_str = json.dumps(weights)
    return json_str


def insert_weight(keyword: str, weight: float, cur:Cursor):
    cur.execute("INSERT INTO weights (keyword, weight) VALUES (?, ?)", (keyword, weight))