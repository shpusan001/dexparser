import { useEffect } from "react";
import ApkListItem from "./ApkListItem";
import { useSelector, useDispatch } from "react-redux";
import { getApkList } from "../module/apk";
import client from "../lib/api/client";

export default function ApkList() {
  const dispatch = useDispatch();
  let apkList = useSelector((state) => state.apk.apkList);

  useEffect(() => {
    dispatch(getApkList());
  }, []);

  return (
    <>
      <h2 class="justify-content-center">APK List</h2>
      {apkList}
      <ApkListItem fileName="냐옹" fileId="냐냐옹" />
    </>
  );
}
