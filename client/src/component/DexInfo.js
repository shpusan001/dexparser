import CodeBox from "../component/CodeBox";
import DexListItem from "../component/DexListItem";
import { useSelector } from "react-redux";
import { useEffect, useState } from "react";
import styled from "styled-components";

const InfoBox = styled.div`
  height: calc(100vh - 225px);
`;

const ListBox = styled.div`
  max-height: calc(100vh - 225px);
`;

export default function DexInfo() {
  let parsedData = useSelector((state) => state.dexInfo.parsing);
  let loading = useSelector((state) => state.loading);
  const [renderedClassList, setRenderedClassList] = useState(null);
  const [renderedFileBtnList, setRenderedBtnList] = useState(null);

  useEffect(() => {
    setRenderedClassList(renderClassList());
    setRenderedBtnList(renderFileBtnList());

    console.log(renderedClassList);
    console.log(renderedFileBtnList);
  }, [loading]);

  const renderFileBtnList = () => {
    if (renderedClassList == null) {
      return;
    }

    const fileBtnList = [];

    for (let i = 0; i < renderedClassList.length; i++) {
      const dexFileBtn = (
        <button key="" class="btn btn-secondary">
          {renderedClassList[i].fileName}
        </button>
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

    const fileList = [];

    for (let i = 0; i < results.length; i++) {
      //file
      const dexFile = results[i];

      fileList.push({ fileName: dexFile.fileName, classList: [] });

      fileList[i].classList.push(
        <DexListItem
          key={String(i)}
          item={{ name: dexFile.fileName, type: "file" }}
        />
      );

      const data = dexFile.data;

      for (let j = 0; j < data.length; j++) {
        //class
        const item = {
          type: "class",
          name: data[j].class,
          superclass: data[j].superclass,
          access: data[j].access_flags,
          interfaces: data[j].interfaces,
          source: data[j].source_file,
        };
        fileList[i].classList.push(
          <DexListItem key={String(i) + "-" + String(j)} item={item} />
        );

        // //static field
        for (let k = 0; k < data[j].class_data.static_fields_size; k++) {
          const staticField = data[j].class_data.static_fields[k];
          const item = {
            type: "field",
            name: staticField.field.name,
            itype: "static",
            ttype: staticField.field.type,
            access: staticField.access_flags,
          };
          fileList[i].classList.push(
            <DexListItem
              key={String(i) + "-" + String(j) + "-sf-" + String(k)}
              item={item}
            />
          );
        }

        //instance field
        for (let k = 0; k < data[j].class_data.instance_fields_size; k++) {
          const instanceField = data[j].class_data.instance_fields[k];
          const item = {
            type: "field",
            name: instanceField.field.name,
            itype: "instance",
            ttype: instanceField.field.type,
            access: instanceField.access_flags,
          };
          fileList[i].classList.push(
            <DexListItem
              key={String(i) + "-" + String(j) + "-if-" + String(k)}
              item={item}
            />
          );
        }

        //direct method
        for (let k = 0; k < data[j].class_data.direct_methods_size; k++) {
          const directMethod = data[j].class_data.direct_methods[k];
          const item = {
            type: "method",
            class: directMethod.method.class,
            name: directMethod.method.name,
            itype: "direct",
            rtype: directMethod.method.proto.return_type,
            access: directMethod.access_flags,
            parameters: directMethod.method.proto.parameters,
            code: directMethod.code.insns,
          };
          fileList[i].classList.push(
            <DexListItem
              key={String(i) + "-" + String(j) + "-df-" + String(k)}
              item={item}
            />
          );
        }

        //virtual
        for (let k = 0; k < data[j].class_data.virtual_methods_size; k++) {
          const virtualMethod = data[j].class_data.virtual_methods[k];
          const item = {
            type: "method",
            class: virtualMethod.method.class,
            name: virtualMethod.method.name,
            itype: "virtual",
            rtype: virtualMethod.method.proto.return_type,
            access: virtualMethod.access_flags,
            parameters: virtualMethod.method.proto.parameters,
            code: virtualMethod.code.insns,
          };
          fileList[i].classList.push(
            <DexListItem
              key={String(i) + "-" + String(j) + "-vf-" + String(k)}
              item={item}
            />
          );
        }
      }
    }

    return fileList;
  };

  return (
    <InfoBox>
      <div class="row">
        <ListBox className="col me-2 bg-light p-3 rounded border overflow-auto"></ListBox>
        {renderedFileBtnList}
        <div class="col m2-2 ">
          <CodeBox />
        </div>
      </div>
    </InfoBox>
  );
}
