import { useState } from "react";
import { useDispatch } from "react-redux";
import { deleteApk } from "../module/apk";

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
        <div class="col-9">
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
        <div class="col-3">
          <button type="submit" class="btn btn-danger w-100" onClick={onSubmit}>
            Remove
          </button>
        </div>
      </form>
    </>
  );
}
