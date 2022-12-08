import { useState } from "react";
import { useDispatch } from "react-redux";
import { uploadApk } from "../module/apk";

export default function ApkUploadForm() {
  const [apkFile, setApkFile] = useState(null);
  const dispatch = useDispatch();

  const onChangeApkFileInput = (e) => {
    setApkFile(e.target.files[0]);
  };

  const onSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", apkFile);
    dispatch(uploadApk(formData));
  };

  return (
    <>
      <form class="row row-cols-lg-auto g-3 align-items-center my-3">
        <div class="col-12">
          <div class="input-group">
            <input
              name="apkFileInput"
              type="file"
              accept=".apk"
              class="form-control"
              placeholder="Username"
              onChange={onChangeApkFileInput}
            />
          </div>
        </div>
        <div class="col-12">
          <button type="submit" class="btn btn-primary" onClick={onSubmit}>
            Upload
          </button>
        </div>
      </form>
    </>
  );
}
