import Header from "./Header";

function MainLayout({ children }) {
  return (
    <div className="min-vh-100 bg-light">
      <Header />

      <main className="container py-4">
        {children}
      </main>
    </div>
  );
}

export default MainLayout;
