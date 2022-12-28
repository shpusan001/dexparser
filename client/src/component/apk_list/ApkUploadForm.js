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
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="18"
              height="18"
              fill="currentColor"
              class="bi bi-upload me-1"
              viewBox="0 0 16 16"
            >
              <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z" />
              <path d="M7.646 1.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 2.707V11.5a.5.5 0 0 1-1 0V2.707L5.354 4.854a.5.5 0 1 1-.708-.708l3-3z" />
            </svg>
            Upload
          </button>
        </div>
      </form>
    </>
  );
}
