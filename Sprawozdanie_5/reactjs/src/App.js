import React, { Component } from 'react';
import './App.css';
import gallery from './gallery_1.jpg'


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
      isLoaded: false,
    }
  }

  componentDidMount() {

    fetch('http://127.0.0.1:8000/gallery/', {method: 'GET', mode: 'cors'})
      .then(res => res.json())
      .then(json => {
        this.setState({
          isLoaded: true,
          items: json,
        })
      });
  }

  render() {
    var { isLoaded, items } = this.state;
  
    if(!isLoaded) {
      return <div>Loading...</div>;
    }
    else {
      return (
        <div className="App">
          <header>
            <h1>Galleries</h1>
          </header>
          <div class="emptyDiv"></div>
    
          <div class="container">
            
            <div class="page">
              {items.map(item => (
                <div class="gallery">
                  <h1 key={item.id}>{item.title}</h1>
                  <img src={gallery} alt={"gallery_photo"}/>
                  <p>Owner: {item.author}</p>
                </div>
              ))}
            </div>
          </div>    
    
          <footer></footer>
        </div>
      );
    }
    
  }
}
export default App;
