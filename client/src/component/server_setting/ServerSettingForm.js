import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getApkList, initApkList } from "../../redux/apk";
import { setMainHost } from "../../redux/setting";
import { getSync } from "../../redux/util";

export default function ServerSettingForm() {
  const [inputHost, setInputHost] = useState(null);
  const dispatch = useDispatch();
  const sync = useSelector((state) => state.util.sync);
  const host = useSelector((state) => state.setting.host);

  useEffect(() => {
    if (sync == "sync") {
      alert(host + " is connected.");
    } else if (sync == null) {
      alert(sync + " is disconnected.");
    }
  }, [sync]);

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
            Apply
          </button>
        </div>
      </form>
    </>
  );
}