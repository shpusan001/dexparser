import { Route, Routes } from "react-router-dom";
import ApkListPage from "./pages/APKListPage";
import DexInfoPage from "./pages/DexInfoPage";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<ApkListPage />}></Route>
        <Route path="/list" element={<ApkListPage />}></Route>
        <Route path="/dex" element={<DexInfoPage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
