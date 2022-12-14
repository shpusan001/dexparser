import Header from "../component/Header";
import DexInfo from "../component/DexInfo";
import DexParseForm from "../component/DexParseForm";

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
