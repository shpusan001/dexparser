import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { getParsing } from "../module/dex";
import { useSelector } from "react-redux";
import { ProgressBar } from "react-bootstrap";

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
      <form class="row row-cols-lg-auto g-8 align-items-center my-3 border p-3 rounded">
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
          {!loading.dexInfo_GET_PARSING && (
            <button type="submit" class="btn btn-primary" onClick={onSubmit}>
              Parse
            </button>
          )}
          {loading.dexInfo_GET_PARSING && (
            <div class="container">
              <div class="spinner-border text-primary" role="status"></div>
            </div>
          )}
        </div>
        <div class="col-12 w-100 mt-4 mb-1">
          {loading.dexInfo_GET_PARSING && (
            <ProgressBar striped animated variant="success" now={50} />
          )}
        </div>
      </form>
    </>
  );
}
