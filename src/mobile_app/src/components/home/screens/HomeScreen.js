import React, {useEffect, useState} from 'react';
import {connect} from 'react-redux';

import {Button, Text, Divider} from 'react-native-elements';

import {View} from 'react-native';

import GateButton from '../GateButton';
import UserBoard from '../UserBoard';
import {requestProfile} from '@api';
import {FORM_INIT} from '@constants';

const HomeScreenComponent = ({request, dispatch, navigation}) => {
  const {userId, baseURL, token} = request;
  const [user, setUser] = useState({
    ...FORM_INIT.USER,
    usersdata: FORM_INIT.USER_DATA,
  });

  useEffect(() => {
    if (userId && navigation.isFocused()) {
      requestProfile(userId, baseURL, token, dispatch).then(response => {
        setUser(response.data);
      });
    }
  }, [baseURL, dispatch, token, userId, navigation]);

  return (
    <View>
      {userId === null ? (
        <Text>Cargando perfil...</Text>
      ) : (
        <UserBoard userData={user} />
      )}
      <GateButton />
      <Divider />
      {user.usersdata.accessLevel === 'AL' ? (
        <Button
          title="Gestión de usuarios"
          onPress={() => navigation.navigate('UserManagement')}
        />
      ) : (
        <View />
      )}
      <Button
        title="Opciones"
        onPress={() => navigation.navigate('Settings')}
      />
    </View>
  );
};

export const HomeScreen = connect(state => state)(HomeScreenComponent);
