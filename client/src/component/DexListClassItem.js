import { useEffect, useState } from "react";
import DexListItem from "./DexListItem";

export default function DexListClassItem(props) {
  const [item, setItem] = useState(props.item);
  const [fileId, setFileId] = useState(item.file_id);
  const [name, setName] = useState(item.name);
  const [type, setType] = useState(item.type);
  const [access, setAccess] = useState(item.access);
  const [interfaces, setInterfaces] = useState(item.interfaces);
  const [superclass, setSuperclass] = useState(item.superclass);
  const [source, setSource] = useState(item.source);
  const [classData, setClassData] = useState(item.class_data);

  const [classItemList, setClassItemList] = useState([]);
  const [isShow, setIsShow] = useState(false);

  useEffect(() => {
    if (access != undefined) {
      let tmpAccess = "";
      for (let i = 0; i < access.length; i++) {
        tmpAccess = tmpAccess + access[i] + " ";
      }
      setAccess(tmpAccess);
    }
  }, []);

  const onClick = () => {
    if (isShow == true) {
      setClassItemList([]);
      setIsShow(false);
      return;
    } else {
      setIsShow(true);
    }

    const tmpClassListItems = [];

    //static field
    for (let i = 0; i < classData.static_fields_size; i++) {
      const staticField = classData.static_fields[i];
      const item = {
        type: "field",
        name: staticField.field.name,
        itype: "static",
        ttype: staticField.field.type,
        access: staticField.access_flags,
      };
      tmpClassListItems.push(
        <DexListItem
          key={String(fileId) + "-" + String(name) + "-sf-" + String(i)}
          item={item}
        />
      );
    }

    //instance field
    for (let i = 0; i < classData.instance_fields_size; i++) {
      const instanceField = classData.instance_fields[i];
      const item = {
        type: "field",
        name: instanceField.field.name,
        itype: "instance",
        ttype: instanceField.field.type,
        access: instanceField.access_flags,
      };
      tmpClassListItems.push(
        <DexListItem
          key={String(fileId) + "-" + String(name) + "-if-" + String(i)}
          item={item}
        />
      );
    }

    //direct method
    for (let i = 0; i < classData.direct_methods_size; i++) {
      const directMethod = classData.direct_methods[i];
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
      tmpClassListItems.push(
        <DexListItem
          key={String(fileId) + "-" + String(name) + "-dm-" + String(i)}
          item={item}
        />
      );
    }

    //virtual
    for (let i = 0; i < classData.virtual_methods_size; i++) {
      const virtualMethod = classData.virtual_methods[i];
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
      tmpClassListItems.push(
        <DexListItem
          key={String(fileId) + "-" + String(name) + "-vm-" + String(i)}
          item={item}
        />
      );
    }
    setClassItemList(tmpClassListItems);
  };

  return (
    <>
      <div class="list-group w-auto mb-2 ms-2" onClick={onClick}>
        <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between">
          <div>
            <h6 class="mb-0 text-break">{props.item.name}</h6>
            <p class="mb-0 opacity-75 text-break">type: {type}</p>
            <p class="mb-0 opacity-75 text-break">superclass: {superclass}</p>
            <p class="mb-0 opacity-75 text-break">access: {access}</p>
            <p class="mb-0 opacity-75 text-break">interfaces: {interfaces}</p>
            <p class="mb-0 opacity-75 text-break">source: {source}</p>
          </div>
        </div>
      </div>
      {classItemList}
    </>
  );
}
