function SourceList({ sources = [] }) {
  if (sources.length === 0) {
    return null;
  }

  return (
    <div className="mt-2">
      <p className="small fw-semibold mb-2">Sources</p>

      <div className="d-flex flex-column gap-2">
        {sources.map((source, index) => (
          <a
            key={`${source.document}-${source.page}-${index}`}
            href={source.url}
            target="_blank"
            rel="noopener noreferrer"
            className="small text-decoration-none"
          >
            {source.title || source.document}
            {source.page != null && ` — page ${source.page}`}
          </a>
        ))}
      </div>
    </div>
  );
}

export default SourceList;