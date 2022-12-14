import { useState } from "react";
import { useDispatch } from "react-redux";
import { uploadApk } from "../../redux/apk";

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
      <h2>File Upload</h2>
      <form class="row g-3 align-items-center my-3 border rounded p-3">
        <div class="col-9">
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
        <div class="col-3">
          <button
            type="submit"
            class="btn btn-primary w-100"
            onClick={onSubmit}
          >
            Upload
          </button>
        </div>
      </form>
    </>
  );
}
