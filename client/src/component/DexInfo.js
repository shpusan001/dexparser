import CodeBox from "../component/CodeBox";
import DexListItem from "../component/DexListItem";
import { useSelector } from "react-redux";
import { useEffect } from "react";

export default function DexInfo() {
  let parsedData = useSelector((state) => state.dexInfo.parsing);
  let loading = useSelector((state) => state.loading);

  useEffect(() => {
    console.log(parsedData);
  }, [loading]);

  const renderClassList = () => {
    if (parsedData == null) {
      return;
    }

    const results = parsedData.results;

    for (let i = 0; i < results.length; i++) {
      const dexFile = results[i];
    }
  };

  return (
    <>
      <div class="row">
        {loading.dexInfo_GET_PARSING && <div>로딩 중</div>}
        <div class="col me-2 bg-primary">
          <DexListItem info={{ type: "type", name: "name" }} />
        </div>
        <div class="col m2-2">
          <CodeBox />
        </div>
      </div>
    </>
  );
}
