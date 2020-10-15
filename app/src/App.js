import React from 'react';
import './App.css';
const axios = require('axios').default;

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {data: undefined};
        this.handleClick = this.handleClick.bind(this);
    }

    componentDidMount() {
        axios.get('http://52.90.81.238/user-info', {withCredentials: true})
            .then((response) => {
                this.setState({data: response.data})
            })
            .catch((error) => {
                this.setState({data: null})
            })
    }

    handleClick() {
        const clientId = "7131016";
        const redirectUri = "http://52.90.81.238/code";
        const display = "page";
        const scope = "friends,offline";
        const responseType = "code";
        this.setState({test: 'ok'})
        window.location.href = `https://oauth.vk.com/authorize?client_id=${clientId}&display=${display}&redirect_uri=${redirectUri}&scope${scope}=&response_type=${responseType}&v=5.101`;
    }

    render() {
        const data = this.state.data;
        if (data === undefined) {
            return null
        } else if (data === null) {
            return (
                <div className="btndiv">
                    <button
                        className="btn"
                        onClick={this.handleClick}
                    >
                        Авторизоваться
                    </button>
                </div>
            )
        } else {
            return (
                <div className="resdiv">
                    <p className='res'>{this.state.data.user.response[0].first_name} {this.state.data.user.response[0].last_name}</p>
                    <p className='res'>Друзья:</p>
                    <ul>
                        {this.state.data.friends.response.items.map((item) => <li className='res'>{item.first_name} {item.last_name}</li>)}
                    </ul>
                </div>
            )
        }
    }
}

export default App;
