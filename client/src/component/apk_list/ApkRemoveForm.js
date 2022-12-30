import { useState } from "react";
import { useDispatch } from "react-redux";
import { deleteApk } from "../../redux/apk";

export default function ApkRemoveForm() {
  const [fileId, setFileId] = useState(null);
  const dispatch = useDispatch();

  const onChangeFileId = (e) => {
    setFileId(e.target.value);
  };

  const onSubmit = (e) => {
    e.preventDefault();
    new Promise((resolve, reject) => {
      resolve(dispatch(deleteApk({ fileId: fileId })));
    }).then(() => {
      setFileId("");
    });
  };
  return (
    <>
      <h2>File Remove</h2>
      <form class="row g-3 align-items-center my-3 border rounded p-3">
        <div class="col-12">
          <div class="input-group">
            <input
              name="fileId"
              type="text"
              class="form-control"
              placeholder="File ID"
              onChange={onChangeFileId}
              value={fileId}
            />
          </div>
        </div>
        <div class="col-12">
          <button type="submit" class="btn btn-danger w-100" onClick={onSubmit}>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="18"
              height="18"
              fill="currentColor"
              class="bi bi-eraser-fill me-1"
              viewBox="0 0 16 16"
            >
              <path d="M8.086 2.207a2 2 0 0 1 2.828 0l3.879 3.879a2 2 0 0 1 0 2.828l-5.5 5.5A2 2 0 0 1 7.879 15H5.12a2 2 0 0 1-1.414-.586l-2.5-2.5a2 2 0 0 1 0-2.828l6.879-6.879zm.66 11.34L3.453 8.254 1.914 9.793a1 1 0 0 0 0 1.414l2.5 2.5a1 1 0 0 0 .707.293H7.88a1 1 0 0 0 .707-.293l.16-.16z" />
            </svg>
            Remove
          </button>
        </div>
      </form>
    </>
  );
}
