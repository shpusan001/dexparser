import { useEffect, useState } from "react";
import ApkListItem from "./ApkListItem";
import { useSelector, useDispatch } from "react-redux";
import { getApkList } from "../module/apk";
import client from "../lib/api/client";

export default function ApkList() {
  const dispatch = useDispatch();
  let apkList = useSelector((state) => state.apk.apkList);

  let [fileList, setFileList] = useState([]);

  useEffect(() => {
    dispatch(getApkList());
  }, []);

  useEffect(() => {
    if (apkList.files != null) {
      setFileList(
        apkList.files.map((e, i) => (
          <ApkListItem
            key={i}
            fileName={e.fileName}
            fileId={e.fileId}
            sha1={e.sha1}
          />
        ))
      );
    }
  }, [apkList]);

  return (
    <>
      <h2 class="justify-content-center">APK List</h2>
      {fileList}
    </>
  );
}
