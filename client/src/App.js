import { Route, Routes } from "react-router-dom";
import ApkListPage from "./pages/APKListPage";
import ResultPage from "./pages/ResultPage";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<ApkListPage />}></Route>
        <Route path="/list" element={<ApkListPage />}></Route>
        <Route path="/dex" element={<ResultPage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
