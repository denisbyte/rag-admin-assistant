function Loader() {
  return (
    <div className="d-flex align-items-center gap-2 text-secondary mb-3">
      <div
        className="spinner-border spinner-border-sm"
        role="status"
        aria-hidden="true"
      />

      <span>Recherche dans les documents...</span>
    </div>
  );
}

export default Loader;