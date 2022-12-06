import { combineReducers } from "redux";
import apk from "./apk";
import dexInfo from "./dexInfo";
import { apkSaga } from "./apk";
import { all } from "redux-saga/effects";

const rootReducer = combineReducers({ apk, dexInfo });

export function* rootSaga() {
  yield all([apkSaga]);
}

export default rootReducer;
