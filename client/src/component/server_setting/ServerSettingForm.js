import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getApkList, initApkList } from "../../redux/apk";
import { setMainHost } from "../../redux/setting";
import { getSync } from "../../redux/util";

export default function ServerSettingForm() {
  const [inputHost, setInputHost] = useState(null);
  const [isInit, setIsInit] = useState(true);
  const dispatch = useDispatch();
  const sync = useSelector((state) => state.util.sync);
  const time = useSelector((state) => state.util.time);
  const host = useSelector((state) => state.setting.host);

  // useEffect(() => {
  //   if (isInit == false) {
  //     if (sync == "sync") {
  //       alert(host + " connection success.");
  //     } else if (sync == null) {
  //       alert(host + " connection failure.");
  //     }
  //   }
  //   setIsInit(false);
  // }, [time]);

  useEffect(() => {
    dispatch(getSync());
  }, [host]);

  const onChangeHostInput = (e) => {
    setInputHost(e.target.value);
  };

  const onSubmit = (e) => {
    e.preventDefault();
    dispatch(setMainHost(inputHost));

    dispatch(initApkList());
  };

  return (
    <>
      <h2>Host</h2>
      <form class="row g-3 align-items-center my-3 border rounded p-3">
        <h3>Current Host</h3>
        {sync == "sync" && (
          <h4 class="text-center text-success bg-light rounded p-2">{host}</h4>
        )}
        {sync == null && (
          <h4 class="text-center text-danger bg-light rounded p-2">{host}</h4>
        )}
        <hr />
        <h3>Host Setting</h3>
        <div class="col-9">
          <div class="input-group">
            <input
              name="hostInput"
              type="text"
              class="form-control"
              placeholder="Host"
              onChange={onChangeHostInput}
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
              class="bi bi-server me-1"
              viewBox="0 0 16 16"
            >
              <path d="M1.333 2.667C1.333 1.194 4.318 0 8 0s6.667 1.194 6.667 2.667V4c0 1.473-2.985 2.667-6.667 2.667S1.333 5.473 1.333 4V2.667z" />
              <path d="M1.333 6.334v3C1.333 10.805 4.318 12 8 12s6.667-1.194 6.667-2.667V6.334a6.51 6.51 0 0 1-1.458.79C11.81 7.684 9.967 8 8 8c-1.966 0-3.809-.317-5.208-.876a6.508 6.508 0 0 1-1.458-.79z" />
              <path d="M14.667 11.668a6.51 6.51 0 0 1-1.458.789c-1.4.56-3.242.876-5.21.876-1.966 0-3.809-.316-5.208-.876a6.51 6.51 0 0 1-1.458-.79v1.666C1.333 14.806 4.318 16 8 16s6.667-1.194 6.667-2.667v-1.665z" />
            </svg>
            Connect
          </button>
        </div>
      </form>
    </>
  );
}
