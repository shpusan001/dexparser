import Header from "../component/common/Header";
import ServerSettingForm from "../component/server_setting/ServerSettingForm";

export default function SettingPage() {
  return (
    <>
      <Header />
      <div class="container mt-3">
        <h1>Setting</h1>
        <hr />
        <ServerSettingForm />
      </div>
    </>
  );
}
