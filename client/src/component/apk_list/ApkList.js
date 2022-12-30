import { useEffect, useState } from "react";
import ApkListItem from "./ApkListItem";
import { useSelector, useDispatch } from "react-redux";
import apk, { getApkList, initApkList } from "../../redux/apk";

export default function ApkList(props) {
  const dispatch = useDispatch();
  let loading = useSelector((state) => state.loading);
  let apkList = useSelector((state) => state.apk.apkList);

  let [fileList, setFileList] = useState([]);

  useEffect(() => {
    dispatch(getApkList());
  }, []);

  useEffect(() => {
    renderApkList();
  }, [apkList]);

  useEffect(() => {
    dispatch(getApkList());
    console.log(loading.apk_UPLOAD_APK);
  }, [loading.apk_UPLOAD_APK, loading.apk_DELETE_APK]);

  const refresh = () => {
    dispatch(getApkList());
  };

  const renderApkList = () => {
    if (apkList != null && apkList != undefined) {
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
    }
  };

  return (
    <div class="pb-3">
      <h2 class="justify-content-center">APK List</h2>
      {/* <div onClick={refresh}>새로고침</div> */}
      <div class="rounded border p-4 mt-3">{fileList}</div>
    </div>
  );
}
