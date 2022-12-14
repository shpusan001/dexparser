import CodeBox from "../component/CodeBox";
import DexListItem from "../component/DexListItem";
import { useSelector } from "react-redux";
import { useEffect, useState } from "react";
import styled from "styled-components";

const ListBox = styled.div`
  max-height: calc(100vh - 315px);
  margin-bottom: 15px;
`;

export default function DexInfo() {
  let parsedData = useSelector((state) => state.dexInfo.parsing);
  let loading = useSelector((state) => state.loading);
  const [renderedClassList, setRenderedClassList] = useState(null);
  const [renderedFileBtnList, setRenderedBtnList] = useState(null);
  const [selectedClassList, setSelectedClassList] = useState(<></>);

  useEffect(() => {
    setRenderedClassList(renderClassList());
  }, [loading]);

  useEffect(() => {
    setRenderedBtnList(renderFileBtnList());
  }, [renderedClassList]);

  const renderFileBtnList = () => {
    if (renderedClassList == null || parsedData == null) {
      return;
    }

    const fileBtnList = [];
    const fileId = parsedData.fileId;

    for (let i = 0; i < renderedClassList.length; i++) {
      const onClick = () => {
        setSelectedClassList(renderedClassList[i].classList);
      };

      const dexFileBtn = (
        <span class="col" key={String(fileId) + "-btn-" + String(i)}>
          <button class="btn btn-secondary w-100" onClick={onClick}>
            {renderedClassList[i].fileName}
          </button>
        </span>
      );
      fileBtnList.push(dexFileBtn);
    }

    return fileBtnList;
  };

  const renderClassList = () => {
    if (parsedData == null) {
      return;
    }

    const results = parsedData.results;
    const fileId = parsedData.fileId;

    const fileList = [];

    for (let i = 0; i < results.length; i++) {
      //file
      const dexFile = results[i];

      fileList.push({ fileName: dexFile.fileName, classList: [] });

      fileList[i].classList.push(
        <DexListItem
          key={String(fileId) + "-" + String(i)}
          item={{ name: dexFile.fileName, type: "file" }}
        />
      );

      const data = dexFile.data;

      for (let j = 0; j < data.length; j++) {
        //class
        const item = {
          file_id: fileId,
          type: "class",
          name: data[j].class,
          superclass: data[j].superclass,
          access: data[j].access_flags,
          interfaces: data[j].interfaces,
          source: data[j].source_file,
          class_data: data[j].class_data,
        };
        fileList[i].classList.push(
          <DexListItem
            key={String(fileId) + "-" + String(i) + "-" + String(j)}
            item={item}
          />
        );
      }
    }

    return fileList;
  };

  return (
    <>
      <div class="p-2 mb-3 mt-3 row row-cols-2 row-cols-lg-5 g-2 g-lg-3 border rounded">
        {renderedFileBtnList}
      </div>

      <div class="row">
        <ListBox className="col me-2 bg-light p-3 rounded border overflow-auto">
          {selectedClassList}
        </ListBox>
        <CodeBox />
      </div>
    </>
  );
}
