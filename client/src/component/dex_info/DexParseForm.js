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
  const [pollingPeriod, setPollingPeriod] = useState(200);
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
        dispatch(
          getProgress({
            reqKey: reqKey,
            nowValue: nowValue,
            maxValue: maxValue,
          })
        );
      }, pollingPeriod);
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
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="18"
                height="18"
                fill="currentColor"
                class="bi bi-cpu me-1"
                viewBox="0 0 16 16"
              >
                <path d="M5 0a.5.5 0 0 1 .5.5V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2h1V.5a.5.5 0 0 1 1 0V2A2.5 2.5 0 0 1 14 4.5h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14v1h1.5a.5.5 0 0 1 0 1H14a2.5 2.5 0 0 1-2.5 2.5v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14h-1v1.5a.5.5 0 0 1-1 0V14A2.5 2.5 0 0 1 2 11.5H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2v-1H.5a.5.5 0 0 1 0-1H2A2.5 2.5 0 0 1 4.5 2V.5A.5.5 0 0 1 5 0zm-.5 3A1.5 1.5 0 0 0 3 4.5v7A1.5 1.5 0 0 0 4.5 13h7a1.5 1.5 0 0 0 1.5-1.5v-7A1.5 1.5 0 0 0 11.5 3h-7zM5 6.5A1.5 1.5 0 0 1 6.5 5h3A1.5 1.5 0 0 1 11 6.5v3A1.5 1.5 0 0 1 9.5 11h-3A1.5 1.5 0 0 1 5 9.5v-3zM6.5 6a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5h-3z" />
              </svg>
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
