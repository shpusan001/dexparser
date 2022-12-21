import { Route, Routes } from "react-router-dom";
import ApkListPage from "./pages/APKListPage";
import DexInfoPage from "./pages/DexInfoPage";
import SettingPage from "./pages/SettingPage";
import client from "./util/api/client";
import { useDispatch, useSelector } from "react-redux";

function App() {
  const host = useSelector((state) => state.setting.host);
  client.defaults.baseURL = host;
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<ApkListPage />}></Route>
        <Route path="/list" element={<ApkListPage />}></Route>
        <Route path="/dex" element={<DexInfoPage />}></Route>
        <Route path="/setting" element={<SettingPage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
