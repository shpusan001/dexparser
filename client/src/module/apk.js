import { createAction, handleActions } from "redux-actions";
import createRequestSaga, {
  createRequestActionTypes,
} from "../lib/createRequestSaga";
import * as apkAPI from "../lib/api/apk";
import { takeLatest } from "redux-saga/effects";

const [GET_APKLIST, GET_APKLIST_SUCCESS, GET_APKLIST_FAILURE] =
  createRequestActionTypes("apk_GET_APKLIST");
const [UPLOAD_APK, UPLOAD_APK_SUCCESS, UPLOAD_APK_FAILURE] =
  createRequestActionTypes("apk_UPLOAD_APK");
const [DELETE_APK, DELETE_APK_SUCCESS, DELETE_APK_FAILURE] =
  createRequestActionTypes("apk_DELETE_APK");

export const getApkList = createAction(GET_APKLIST, (data) => data);
export const uploadApk = createAction(UPLOAD_APK, (data) => data);
export const deleteApk = createAction(DELETE_APK, (data) => data);

//사가 생성
const getApkListSaga = createRequestSaga(GET_APKLIST, apkAPI.getAPIList);
const uploadApkSaga = createRequestSaga(UPLOAD_APK, apkAPI.uploadApkFile);
const deleteApkSaga = createRequestSaga(DELETE_APK, apkAPI.deleteApkFile);

export function* apkSaga() {
  yield takeLatest(GET_APKLIST, getApkListSaga);
  yield takeLatest(UPLOAD_APK, uploadApkSaga);
  yield takeLatest(DELETE_APK, deleteApkSaga);
}

const initialState = {
  apkList: null,
  upload: null,
  delete: null,
  error: null,
};

const apk = handleActions(
  {
    [GET_APKLIST_SUCCESS]: (state, { payload: data }) => ({
      ...state,
      apkList: data,
      error: null,
    }),
    [GET_APKLIST_FAILURE]: (state, { payload: error }) => ({
      ...state,
      apkList: null,
      error: error,
    }),
    [UPLOAD_APK_SUCCESS]: (state, { payload: data }) => {
      return {
        ...state,
        upload: data,
        error: null,
      };
    },
    [UPLOAD_APK_FAILURE]: (state, { payload: error }) => {
      return {
        ...state,
        upload: null,
        error: error,
      };
    },
    [DELETE_APK_SUCCESS]: (state, { payload: data }) => ({
      ...state,
      delete: data,
      error: null,
    }),
    [DELETE_APK_FAILURE]: (state, { payload: error }) => {
      return {
        ...state,
        delete: null,
        error: error,
      };
    },
  },
  initialState
);

export default apk;
