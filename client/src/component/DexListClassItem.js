import { useEffect, useState } from "react";

export default function DexListClassItem(props) {
  const [item, setItem] = useState(props.item);
  const [name, setName] = useState(item.name);
  const [type, setType] = useState(item.type);
  const [access, setAccess] = useState(item.access);
  const [interfaces, setInterfaces] = useState(item.interfaces);
  const [superclass, setSuperclass] = useState(item.superclass);
  const [source, setSource] = useState(item.source);

  useEffect(() => {
    if (access != undefined) {
      let tmpAccess = "";
      for (let i = 0; i < access.length; i++) {
        tmpAccess = tmpAccess + access[i] + " ";
      }
      setAccess(tmpAccess);
    }
  }, []);

  return (
    <>
      <div class="list-group w-auto mb-2 ms-2">
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
    </>
  );
}
