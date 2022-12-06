import { createAction, handleActions } from "redux-actions";
import createRequestSaga, {
  createRequestActionTypes,
} from "../lib/createRequestSaga";
import * as apkAPI from "../lib/api/apk";
import { takeLatest } from "redux-saga/effects";

const [GET_PARSING, GET_PARSING_SUCCESS, GET_PARSING_FAILURE] =
  createRequestActionTypes("dexInfo/GET_PARSING");
const [
  GET_CONV_HEX2SMALI,
  GET_CONV_HEX2SMALI_SUCCESS,
  GET_CONV_HEX2SMALI_FAILURE,
] = createRequestActionTypes("dexInfo/GET_CONV_HEX2SMALI");

export const getApkList = createAction(GET_PARSING, (data) => data);
export const uploadApk = createAction(GET_CONV_HEX2SMALI, (data) => data);

//사가 생성
const getApkListSaga = createRequestSaga(GET_PARSING, apkAPI.getAPIList);
const uploadApkSaga = createRequestSaga(
  GET_CONV_HEX2SMALI,
  apkAPI.uploadApkFile
);

export function* dexInfoSaga() {
  yield takeLatest(GET_PARSING, getApkListSaga);
  yield takeLatest(GET_CONV_HEX2SMALI, uploadApkSaga);
}

const initialState = {
  parsing: null,
  smali: null,
  error: null,
};

const apkList = handleActions(
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
  },
  initialState
);

export default apkList;
