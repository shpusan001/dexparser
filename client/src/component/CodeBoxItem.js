import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import Highlight from "react-highlight";
import hljs from "highlight.js";
import "highlight.js/styles/androidstudio.css";
import smali from "highlight.js/lib/languages/smali";

export default function CodeBoxItem(props) {
  const loading = useSelector((state) => state.loading);
  const [item, setItem] = useState(props.item);
  const [line, setLine] = useState(item.line);
  const [code, setCode] = useState(item.code);

  // useEffect(() => {
  //   hljs.registerLanguage("smali", smali);
  //   const highlihgtedCode = hljs.highlight(code, { language: "smali" }).value;
  //   setCode(highlihgtedCode);
  //   hljs.highlightAll();
  // }, []);

  return (
    <>
      <div class="list-group w-auto mb-2 ">
        <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between">
          <div class="row">
            <p class="col mb-0 opacity-75 text-break text-primary">{line}</p>
            <p class="col-sm-12 mb-0 opacity-75 text-break code">{code}</p>
          </div>
        </div>
      </div>
    </>
  );
}
