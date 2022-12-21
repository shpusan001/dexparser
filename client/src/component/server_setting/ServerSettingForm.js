import { useState } from "react";
import { useDispatch } from "react-redux";
import { setMainHost } from "../../redux/setting";
import client from "../../util/api/client";

export default function ServerSettingForm() {
  const [host, setHost] = useState(null);
  const dispatch = useDispatch();

  const onChangeHostInput = (e) => {
    setHost(e.target.value);
  };

  const onSubmit = (e) => {
    e.preventDefault();
    dispatch(setMainHost(host));
  };

  return (
    <>
      <h2>Server</h2>
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
