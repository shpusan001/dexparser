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

    const classList = [];

    for (let i = 0; i < results.length; i++) {
      const dexFile = results[i];
      classList.push(
        <DexListItem info={{ name: dexFile.fileName, type: "file" }} />
      );
      const data = dexFile.data;
      for (let j = 0; j < data.length; j++) {
        classList.push(
          <DexListItem info={{ name: data[j].class, type: "class" }} />
        );
      }
    }

    return classList;
  };

  return (
    <>
      <div class="row">
        {loading.dexInfo_GET_PARSING && <div>로딩 중</div>}
        <div class="col me-2 bg-primary">{renderClassList()}</div>
        <div class="col m2-2">
          <CodeBox />
        </div>
      </div>
    </>
  );
}
