import './App.css';

function App() {
  return (
    <div className='formulaire'>
      <form>
        <div className="mb-3 divIn">
          <label for="exampleInputUser1" class="form-label">Utilisateur : </label>
          <input type="text" class="form-control" id="exampleInputUser1" placeholder='Saisir l utilisateur'/>
        </div>
        <div className="mb-3 divIn">
          <label for="exampleInputEmail1" class="form-label">Email : </label>
          <input type="email" class="form-control" id="exampleInputEmail1" placeholder='Saisir l email'/>
        </div>
        <button type="submit p-2" className="btn btn-primary divIn">Valider</button>
      </form>

      <table class="table table-striped">
        <thead>
          <tr>
            <th>Client</th>
            <th>Liste des ventes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Nom</td>
            <td>Ventes</td>
          </tr>
          <tr>
            <td>Nom</td>
            <td>Ventes</td>
          </tr>
          <tr>
            <td>Nom</td>
            <td>Ventes</td>
          </tr>
        </tbody>
      </table>
    </div>      
  );
}

export default App;
