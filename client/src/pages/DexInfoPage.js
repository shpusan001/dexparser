import Header from "../component/common/Header";
import DexInfo from "../component/dex_info/DexInfo";
import DexParseForm from "../component/dex_info/DexParseForm";

export default function DexInfoPage() {
  return (
    <>
      <Header />
      <div class="container mt-3">
        <h1>DexInfo</h1>
        <hr />
        <div class="ms-3">
          <DexParseForm />
          <DexInfo />
        </div>
      </div>
    </>
  );
}
