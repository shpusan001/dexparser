import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { getParsing, getProgress } from "../../redux/dex";
import { useSelector } from "react-redux";
import { ProgressBar } from "react-bootstrap";
import { getUUIDv4 } from "../../util/uuid";

export default function DexParseForm() {
  const [fileId, setFileId] = useState(null);
  const [nowValue, setNowValue] = useState(0);
  const [maxValue, setMaxValue] = useState(0);
  const [reqKey, setReqKey] = useState("");
  const [intervalId, setIntervalId] = useState(-1);
  const dispatch = useDispatch();

  let loading = useSelector((state) => state.loading);
  let progress = useSelector((state) => state.dexInfo.progress);

  const onChangeFileId = (e) => {
    setFileId(e.target.value);
  };

  const onSubmit = (e) => {
    const genReqKey = getUUIDv4();
    dispatch(getParsing({ fileId: fileId, reqKey: genReqKey }));
    setReqKey(genReqKey);
    e.preventDefault();
  };

  const dispatchProgress = (flag) => {
    if (flag == true) {
      const tmp = setInterval(() => {
        console.log("hi");
        dispatch(
          getProgress({
            reqKey: reqKey,
            nowValue: nowValue,
            maxValue: maxValue,
          })
        );
      }, 1000);
      setIntervalId(tmp);
    } else {
      setNowValue(0);
      setMaxValue(0);
      clearInterval(intervalId);
    }
  };

  useEffect(() => {
    dispatchProgress(loading.dexInfo_GET_PARSING);
  }, [loading.dexInfo_GET_PARSING]);

  useEffect(() => {
    if (progress != null) {
      setNowValue(progress.nowValue);
      setMaxValue(progress.maxValue);
    }
  }, [loading.dexInfo_GET_PROGRESS]);

  return (
    <>
      <form class="row my-3 border p-3 rounded">
        <div class="col-10">
          <div class="input-group ">
            <input
              type="text"
              class="form-control"
              placeholder="File ID"
              onChange={onChangeFileId}
            />
          </div>
        </div>
        <div class="col-2">
          {!loading.dexInfo_GET_PARSING && (
            <button
              type="submit"
              class="btn btn-primary w-100"
              onClick={onSubmit}
            >
              Parse
            </button>
          )}
          {loading.dexInfo_GET_PARSING && (
            <div class="container col-2 align-items-center">
              <div class="spinner-border text-primary" role="status"></div>
            </div>
          )}
        </div>
        <div class="col w-100 mt-4 mb-1">
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
