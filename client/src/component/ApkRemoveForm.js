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
      resolve(dispatch(deleteApk({ fileId: fileId })))
    }).then(()=>{
      setFileId("")
    })
  };
  return (
    <>
      <form class="row row-cols-lg-auto g-3 align-items-center my-3">
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
          <button type="submit" class="btn btn-danger" onClick={onSubmit}>
            Remove
          </button>
        </div>
      </form>
    </>
  );
}
