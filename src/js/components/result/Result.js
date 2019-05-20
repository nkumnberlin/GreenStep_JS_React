import React, {Component} from 'react'
import {Divider, Progress, Container, Header, Segment, Grid} from 'semantic-ui-react'

export default class Results extends Component {
    fetchResults = [
        {
            0: {
                transport: 'Plane',
                emission: 21,
                distance: 1000,
                description: 'Fancy things about plane flights are bad!',
                icon: 'tba'
            }
        }, {
            1: {
                transport: 'Car',
                emission: 15,
                distance: 600,
                description: 'Fancy things about car rides are bad!',
                icon: 'tba'
            }
        }, {
            2: {
                transport: 'Train',
                emission: 8,
                distance: 300,
                description: 'Fancy things about train rides are bad!',
                icon: 'tba'
            }
        }
    ];


    _renderFetchResults() {
        return Object.entries(this.fetchResults).map(([key, value], i) => {

                const getHighestEmission = () => {
                    let arr = [];
                    arr.push(value[key].emission)
                    // return(Math.max(...arr))
                    return 21;
                };

                const getHighestDistance = () => {
                    let arr = [];
                    Object.entries(this.fetchResults).map(([key, value]) => {
                        arr.push(value[key].distance)
                    });
                    // return(Math.max(...arr))
                    return 1000;
                };

                const descriptionResults = {
                    typ: 'Type of Transport',
                    dist: 'Distance',
                    em: 'Emission Value',
                    unitWeight: 'kg',
                    unitDistance: 'km',
                    separator: ': '
                };


                const BuildTopProgressbar = (emission) => {
                    const MaxEmission = getHighestEmission() / 100;
                    return 100 - (emission / MaxEmission);
                };

                const BuildBotProgressbar = (distance) => {
                    const MaxEmission = getHighestDistance() / 100;
                    return distance / MaxEmission;
                };


                const BuildProgressbar = (emission, distance) =>
                    <Segment>
                        <Header as='h2'>
                            <p>{value[key].transport}</p>
                        </Header>
                        <Header.Subheader>
                            <Progress content={<p>
                                <br/>{descriptionResults.em + descriptionResults.separator + +value[key].emission + descriptionResults.unitWeight}
                            </p>} percent={BuildTopProgressbar(emission)} indicating/>
                            <p>
                                <br/>{descriptionResults.dist}{descriptionResults.separator}{value[key].distance} {descriptionResults.unitDistance}
                            </p>
                        </Header.Subheader>
                    </Segment>;


                return (
                    <Grid columns={1} key={key}>
                        <Grid.Column>
                            {/*{CreateCO2Bubble(value[key].emission)}*/}
                            {BuildProgressbar(value[key].emission, value[key].distance)}
                        </Grid.Column>
                    </Grid>


                )
            }
        )
    }

    render() {
        return (
            <div>
                <Segment>
                    <Container textAlign='center'><Header as='h1'> Results </Header></Container>
                    <Divider/>
                    <Container fluid textAlign='center'>
                        {this._renderFetchResults()}
                    </Container>
                </Segment>
            </div>
        )
    };
}

