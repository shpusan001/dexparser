import { combineReducers } from "redux";
import dexInfo from "./dex";
import { apkSaga } from "./apk";
import { dexInfoSaga } from "./dex";
import { all } from "redux-saga/effects";
import loading from "./loading";
import apk from "./apk";
import setting from "./setting";

const rootReducer = combineReducers({ loading, apk, dexInfo, setting });

export function* rootSaga() {
  yield all([apkSaga(), dexInfoSaga()]);
}

export default rootReducer;
