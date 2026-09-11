function ErrorMessage({ message }) {
  if (!message) {
    return null;
  }

  return (
    <div className="alert alert-danger mt-3 mb-3" role="alert">
      <strong>Erreur : </strong>
      {message}
    </div>
  );
}

export default ErrorMessage;