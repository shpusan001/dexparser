import { combineReducers } from "redux";
import apk from "./apk";
import dexInfo from "./dexInfo";
import { apkSaga } from "./apk";
import { dexInfoSaga } from "./dexInfo";
import { all } from "redux-saga/effects";
import loading from "./loading";

const rootReducer = combineReducers({ apk, dexInfo, loading });

export function* rootSaga() {
  yield all([apkSaga(), dexInfoSaga()]);
}

export default rootReducer;
