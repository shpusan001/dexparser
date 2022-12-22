import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import CodeListItem from "./CodeListItem";
import styled from "styled-components";

const ListBox = styled.div`
  max-height: calc(100vh - 315px);
  margin-bottom: 15px;
`;

export default function CodeList() {
  const [isInit, setIsInit] = useState(true);
  const smali = useSelector((state) => state.dexInfo.smali);
  const selectedMethod = useSelector((state) => state.dexInfo.selected_method);

  const [renderedCodeList, setRenderedCodeList] = useState(<></>);

  useEffect(() => {
    if (isInit == false) {
      new Promise((resolve, reject) => {
        resolve();
      }).then(() => {
        setRenderedCodeList(renderSmaliList());
      });
    }
    setIsInit(false);
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

      if (typeof e[1] != "string") return <></>;

      const clazz = selectedMethod.class;
      const method = selectedMethod.method;

      return (
        <CodeListItem
          key={String(clazz) + "-" + String(method) + "-" + String(i)}
          item={item}
        />
      );
    });

    return codeList;
  };

  return <>{renderedCodeList}</>;
}
