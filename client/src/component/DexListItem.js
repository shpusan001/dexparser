export default function DexListItem(props) {
  return (
    <>
      <div class="list-group w-auto mb-2">
        <div class=" list-group-item list-group-item-action d-flex gap-3 py-3 d-flex gap-2 w-100 justify-content-between">
          <div>
            <h6 class="mb-0">{props.info.name}</h6>
            <p class="mb-0 opacity-75">type: {props.info.type}</p>
          </div>
        </div>
      </div>
    </>
  );
}
