import { combineReducers } from "redux";
import dexInfo from "./dex";
import { apkSaga } from "./apk";
import { dexInfoSaga } from "./dex";
import { all } from "redux-saga/effects";
import loading from "./loading";
import apk from "./apk";

const rootReducer = combineReducers({ loading, apk, dexInfo });

export function* rootSaga() {
  yield all([apkSaga(), dexInfoSaga()]);
}

export default rootReducer;
