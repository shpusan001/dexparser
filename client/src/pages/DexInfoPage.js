import Header from "../component/Header";
import DexInfo from "../component/DexInfo";
import DexParseForm from "../component/DexParseForm";

export default function DexInfoPage() {
  return (
    <>
      <Header />
      <div class="container h-100">
        <DexParseForm />
        <DexInfo />
      </div>
    </>
  );
}
