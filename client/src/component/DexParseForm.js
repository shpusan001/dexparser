import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { getParsing } from "../module/dex";
import { useSelector } from "react-redux";

export default function DexParseForm() {
  const [fileId, setFileId] = useState(null);
  const dispatch = useDispatch();

  let loading = useSelector((state) => state.loading);

  const onChangeFileId = (e) => {
    setFileId(e.target.value);
  };

  const onSubmit = (e) => {
    dispatch(getParsing({ fileId: fileId }));
    e.preventDefault();
  };

  useEffect(() => {}, [loading]);

  return (
    <>
      <form class="row row-cols-lg-auto g-3 align-items-center my-3">
        <div class="col-12">
          <div class="input-group">
            <input
              type="text"
              class="form-control"
              placeholder="File ID"
              onChange={onChangeFileId}
            />
          </div>
        </div>
        <div class="col-12">
          <button type="submit" class="btn btn-primary" onClick={onSubmit}>
            Parse
          </button>
        </div>
      </form>
    </>
  );
}
