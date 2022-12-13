import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { getParsing, getProgress } from "../module/dex";
import { useSelector } from "react-redux";
import { ProgressBar } from "react-bootstrap";
import { getUUIDv4 } from "../util/uuid";

export default function DexParseForm() {
  const [fileId, setFileId] = useState(null);
  const [nowValue, setNowValue] = useState(0);
  const [maxValue, setMaxValue] = useState(0);
  // const [reqKey, setReqKey] = useState("");
  const dispatch = useDispatch();

  let loading = useSelector((state) => state.loading);
  let progress = useSelector((state) => state.dexInfo.progress);

  const onChangeFileId = (e) => {
    setFileId(e.target.value);
  };

  const onSubmit = (e) => {
    const reqKey = getUUIDv4();
    dispatch(getParsing({ fileId: fileId, reqKey: reqKey }));
    e.preventDefault();
  };

  const dispatchProgress = (reqKey) => {
    dispatch(getProgress({ reqKey: reqKey }));
  };

  useEffect(() => {
    if (progress != null) {
      setNowValue(progress.nowValue);
      setMaxValue(progress.maxValue);
    }
  }, [loading.dexInfo_GET_PROGRESS]);

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
            <ProgressBar
              striped
              animated
              variant="success"
              now={nowValue}
              max={maxValue}
            />
          )}
        </div>
      </form>
    </>
  );
}
