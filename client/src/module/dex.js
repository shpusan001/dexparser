import { createAction, createActions, handleActions } from "redux-actions";
import createRequestSaga, {
  createRequestActionTypes,
} from "../lib/createRequestSaga";
import * as dexAPI from "../lib/api/dex";
import { takeLatest } from "redux-saga/effects";

const [GET_PARSING, GET_PARSING_SUCCESS, GET_PARSING_FAILURE] =
  createRequestActionTypes("dexInfo_GET_PARSING");
const [
  GET_CONV_HEX2SMALI,
  GET_CONV_HEX2SMALI_SUCCESS,
  GET_CONV_HEX2SMALI_FAILURE,
] = createRequestActionTypes("dexInfo_GET_CONV_HEX2SMALI");
const [GET_PROGRESS, GET_PROGRESS_SUCCESS, GET_PROGRESS_FAILURE] =
  createRequestActionTypes("dexInfo_GET_PROGRESS");

const SET_SELECTED_METHOD = "dexInfo_SET_SELECTED_METHOD";

export const getParsing = createAction(GET_PARSING, (data) => data);
export const getConvHex2Smali = createAction(
  GET_CONV_HEX2SMALI,
  (data) => data
);
export const getProgress = createAction(GET_PROGRESS, (data) => data);

export const setSelectedMethod = createAction(
  SET_SELECTED_METHOD,
  (data) => data
);

//사가 생성
const getParsingSaga = createRequestSaga(GET_PARSING, dexAPI.getParsing);
const getConvHex2SmaliSaga = createRequestSaga(
  GET_CONV_HEX2SMALI,
  dexAPI.getSmali
);
const getProgressSaga = createRequestSaga(GET_PROGRESS, dexAPI.getProgress);

export function* dexInfoSaga() {
  yield takeLatest(GET_PARSING, getParsingSaga);
  yield takeLatest(GET_CONV_HEX2SMALI, getConvHex2SmaliSaga);
  yield takeLatest(GET_PROGRESS, getProgressSaga);
}

const initialState = {
  parsing: null,
  smali: null,
  selected_method: null,
  error: null,
  progress: null,
  progress_error: null,
};

const dexInfo = handleActions(
  {
    [GET_PARSING_SUCCESS]: (state, { payload: data }) => ({
      ...state,
      parsing: data,
      error: null,
    }),
    [GET_PARSING_FAILURE]: (state, { payload: error }) => ({
      ...state,
      parsing: null,
      error: error,
    }),
    [GET_CONV_HEX2SMALI_SUCCESS]: (state, { payload: data }) => {
      return {
        ...state,
        smali: data,
        error: null,
      };
    },
    [GET_CONV_HEX2SMALI_FAILURE]: (state, { payload: error }) => {
      return {
        ...state,
        smali: null,
        error: error,
      };
    },
    [SET_SELECTED_METHOD]: (state, { payload: data }) => {
      return {
        ...state,
        selected_method: data,
      };
    },
    [GET_PROGRESS_SUCCESS]: (state, { payload: data }) => {
      return {
        ...state,
        progress: data,
      };
    },
    [GET_PROGRESS_FAILURE]: (state, { payload: error }) => {
      return {
        ...state,
        progress_error: error,
      };
    },
  },
  initialState
);

export default dexInfo;
