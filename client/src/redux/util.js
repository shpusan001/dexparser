import { createAction, handleActions } from "redux-actions";
import { createRequestActionTypes } from "../util/requestSaga";
import * as utilAPI from "../util/api/util";
import { takeLatest } from "redux-saga/effects";
import createRequestSaga from "../util/requestSaga";

const [GET_SYNC, GET_SYNC_SUCCESS, GET_SYNC_FAILURE] =
  createRequestActionTypes("util_GET_SYNC");

export const getSync = createAction(GET_SYNC, (data) => data);

const getSyncSaga = createRequestSaga(GET_SYNC, utilAPI.getSync);

export function* utilSaga() {
  yield takeLatest(GET_SYNC, getSyncSaga);
}

const initialState = {
  sync: null,
  error: null,
};

const util = handleActions(
  {
    [GET_SYNC_SUCCESS]: (state, { payload: data }) => ({
      ...state,
      sync: "data",
      error: null,
    }),
  },
  {
    [GET_SYNC_FAILURE]: (state, { payload: error }) => ({
      ...state,
      sync: null,
      error: error,
    }),
  },
  initialState
);

export default util;
