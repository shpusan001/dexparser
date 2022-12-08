import { useEffect, useState } from "react";

export default function DexListItem(props) {
  const [info, setInfo] = useState(props.info);
  const [name, setName] = useState(info.name);
  const [type, setType] = useState(info.type);
  const [access, setAccess] = useState(info.access);

  const [superclass, setSuperclass] = useState(null);

  const [itype, setItype] = useState(null);
  const [ttype, setTtype] = useState(null);

  const [parameters, setParameters] = useState(null);
  const [rtype, setRtype] = useState(null);

  useEffect(() => {}, []);

  return (
    <>
      <div class="list-group w-auto mb-2">
        <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between">
          <div>
            <h6 class="mb-0 text-break">{props.info.name}</h6>
            <p class="mb-0 opacity-75 text-break">type: {props.info.type}</p>
            <p class="mb-0 opacity-75 text-break">
              access: {props.info.access}
            </p>
            <p class="mb-0 opacity-75 text-break">
              interfaces: {props.info.interfaces}
            </p>
            <p class="mb-0 opacity-75 text-break">source: {props.info.type}</p>
            <p class="mb-0 opacity-75 text-break">
              parameters: {props.info.type}
            </p>
            <p class="mb-0 opacity-75 text-break">return: {props.info.type}</p>
          </div>
        </div>
      </div>
    </>
  );
}
