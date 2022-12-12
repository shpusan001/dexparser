import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { setSelectedMethod } from "../module/dex";
import { startLoading } from "../module/loading";
import CodeBoxItem from "./CodeBoxItem";

export default function CodeBox(props) {
  const loading = useSelector((state) => state.loading);
  const smali = useSelector((state) => state.dexInfo.smali);
  const selectedMethod = useSelector((state) => state.dexInfo.selected_method);

  const [renderedCodeList, setRenderedCodeList] = useState(<></>);

  useEffect(() => {
    new Promise((resolve, reject) => {
      resolve();
    }).then(() => {
      setRenderedCodeList(renderSmaliList());
    });
  }, [smali]);

  const renderSmaliList = () => {
    let codeList = [];

    if (smali == null || smali.smali == null) {
      return;
    }

    codeList = smali.smali.map((e, i) => {
      const item = {
        line: e[0],
        code: e[1],
      };

      const clazz = selectedMethod.class;
      const method = selectedMethod.method;

      return (
        <CodeBoxItem
          key={String(clazz) + "-" + String(method) + "-" + String(i)}
          item={item}
        />
      );
    });

    return codeList;
  };

  return (
    <>
      <div class="border rounded p-4 bg-light">{renderedCodeList}</div>
    </>
  );
}
